"""Service module 39821: business logic, no crypto."""


def calculate_total_39821(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39821():
    return 'module 39821 handles orders and invoices'
