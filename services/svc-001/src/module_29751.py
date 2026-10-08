"""Service module 29751: business logic, no crypto."""


def calculate_total_29751(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29751():
    return 'module 29751 handles orders and invoices'
