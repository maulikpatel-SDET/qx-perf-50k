"""Service module 47936: business logic, no crypto."""


def calculate_total_47936(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47936():
    return 'module 47936 handles orders and invoices'
