"""Service module 39266: business logic, no crypto."""


def calculate_total_39266(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39266():
    return 'module 39266 handles orders and invoices'
