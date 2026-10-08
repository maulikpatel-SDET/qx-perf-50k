"""Service module 18407: business logic, no crypto."""


def calculate_total_18407(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18407():
    return 'module 18407 handles orders and invoices'
