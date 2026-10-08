"""Service module 8421: business logic, no crypto."""


def calculate_total_8421(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8421():
    return 'module 8421 handles orders and invoices'
