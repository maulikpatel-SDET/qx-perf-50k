"""Service module 36856: business logic, no crypto."""


def calculate_total_36856(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36856():
    return 'module 36856 handles orders and invoices'
