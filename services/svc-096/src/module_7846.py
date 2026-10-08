"""Service module 7846: business logic, no crypto."""


def calculate_total_7846(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7846():
    return 'module 7846 handles orders and invoices'
