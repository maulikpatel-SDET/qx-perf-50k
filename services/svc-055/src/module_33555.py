"""Service module 33555: business logic, no crypto."""


def calculate_total_33555(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33555():
    return 'module 33555 handles orders and invoices'
