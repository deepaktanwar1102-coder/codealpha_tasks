# TODO

## Plan checklist (Django DRF + premium frontend)
1. Scaffold backend project (Django + Django REST Framework).
2. Create apps: accounts, products, cart, orders.
3. Implement models + migrations:
   - Users (Django auth)
   - Product
   - CartItem
   - Order
4. Implement authentication (JWT) + protected routes.
5. Implement DRF endpoints:
   - /api/auth/*
   - /api/products
   - /api/cart
   - /api/orders
6. Admin integration for products + stock management.
7. Scaffold frontend (static SPA with multiple pages or simple routing):
   - Home, Product Listing, Product Details, Cart, Checkout, Register/Login, Dashboard.
8. Implement premium UI (dark/light toggle, glass cards, animations, skeletons, modals, toasts, carousel).
9. Wire frontend to backend APIs (cart, wishlist optional, order placement).
10. Add lazy-loading, pagination, filtering/sorting, live search.
11. Run local dev servers; test flows:
   - register/login
   - browse/search/filter
   - add/remove/update cart
   - checkout/order success + order history
12. Document run instructions in README.md.

