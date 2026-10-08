"""Service module 27248: business logic, no crypto."""


def calculate_total_27248(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27248():
    return 'module 27248 handles orders and invoices'
