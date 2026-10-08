"""Service module 43751: business logic, no crypto."""


def calculate_total_43751(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43751():
    return 'module 43751 handles orders and invoices'
