"""Service module 28691: business logic, no crypto."""


def calculate_total_28691(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28691():
    return 'module 28691 handles orders and invoices'
