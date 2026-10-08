"""Service module 2831: business logic, no crypto."""


def calculate_total_2831(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2831():
    return 'module 2831 handles orders and invoices'
