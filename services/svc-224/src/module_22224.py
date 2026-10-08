"""Service module 22224: business logic, no crypto."""


def calculate_total_22224(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22224():
    return 'module 22224 handles orders and invoices'
