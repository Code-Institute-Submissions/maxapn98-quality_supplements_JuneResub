from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from pkg_resources import require
from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm


def all_products(request):
    """ A view to show all products, including sorting and search queries """
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_product_name'
                products = products.annotate(lower_name=Lower('product_name'))

            if sortkey == 'category':
                sortkey = "product_category"

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            products = products.order_by(sortkey)

        if 'category' in request.GET:
            category = request.GET['category'].split(',')
            products = products.filter(
                product_category__product_category__in=category)
            categories = Category.objects.filter(
                product_category__in=category)

            if 'direction' in request.GET:
                direction = request.GET['direction']
                sortkey = "product_category"
                if direction == "desc":
                    sortkey = f'-{sortkey}'

                products = products.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(product_name__icontains=query) | Q(
                product_description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    # Query product from db
    product = get_object_or_404(Product, pk=product_id)
    # Query product's reviews from db 
    reviews = Review.objects.all()
    reviews = reviews.filter(product=product)
    # Create Review form for posting reviews
    form = ReviewForm()

    # Context
    context = {
        "form": form,
        'product': product,
        "reviews": reviews,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
@staff_member_required
def add_product(request):
    """ Add a product to the store """

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
@staff_member_required
def edit_product(request, product_id):
    """ Edit a product in the store """

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.product_name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
@staff_member_required
def delete_product(request, product_id):
    """ Delete a product from the store """

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
@require_POST
def add_review(request, product_id):
    """add review to product"""
    
    reviewForm = ReviewForm(request.POST or None)
    # Check if the review form inputs are valid
    if reviewForm.is_valid():
        # Get body context of the review
        body = request.POST.get("body")

        # Query product that is being reviewed
        product = get_object_or_404(Product, pk=product_id)

        # Create a review object
        review = Review.objects.create(product=product, user=request.user, body=body)
        review.save()
        return redirect(reverse("product_detail", args=(product_id,)))
    else:
        return redirect(reverse("product_detail", args=(product_id,)))