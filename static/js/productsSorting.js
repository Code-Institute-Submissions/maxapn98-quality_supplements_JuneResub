$("#sort-selector").change(function () {
    let selectDropdown = $(this);
    let currentUrl = new URL(window.location);
    let selectedValue = selectDropdown.val();
    if (selectedValue != "reset") {
      let sort = selectedValue.split("_")[0];
      let direction = selectedValue.split("_")[1];
  
      currentUrl.searchParams.set("sort", sort);
      currentUrl.searchParams.set("direction", direction);
  
      window.location.replace(currentUrl);
    } else {
      currentUrl.searchParams.delete("sort");
      currentUrl.searchParams.delete("direction");
  
      window.location.replace(currentUrl);
    }
  });