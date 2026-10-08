"""Service module 45555: business logic, no crypto."""


def calculate_total_45555(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45555():
    return 'module 45555 handles orders and invoices'
