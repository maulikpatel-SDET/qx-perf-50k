"""Service module 39186: business logic, no crypto."""


def calculate_total_39186(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39186():
    return 'module 39186 handles orders and invoices'
