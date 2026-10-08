"""Service module 23555: business logic, no crypto."""


def calculate_total_23555(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23555():
    return 'module 23555 handles orders and invoices'
