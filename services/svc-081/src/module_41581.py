"""Service module 41581: business logic, no crypto."""


def calculate_total_41581(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41581():
    return 'module 41581 handles orders and invoices'
