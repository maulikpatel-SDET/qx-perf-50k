"""Service module 33968: business logic, no crypto."""


def calculate_total_33968(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33968():
    return 'module 33968 handles orders and invoices'
