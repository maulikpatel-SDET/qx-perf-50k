"""Service module 20555: business logic, no crypto."""


def calculate_total_20555(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20555():
    return 'module 20555 handles orders and invoices'
