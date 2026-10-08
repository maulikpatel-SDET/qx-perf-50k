"""Service module 38801: business logic, no crypto."""


def calculate_total_38801(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38801():
    return 'module 38801 handles orders and invoices'
