from .products import (
    ProductCreateView, ProductUpdateView, ProductDeleteView,
    ProductListView, ProductJsonListView,
    product_create, product_update, product_delete,
    product_list, product_detail, product_detail_by_url_key
)
from .categories import (
    CategoryList, CategoryDetail,
    category_list, category_detail
)