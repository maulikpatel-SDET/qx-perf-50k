"""Service module 41691: business logic, no crypto."""


def calculate_total_41691(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41691():
    return 'module 41691 handles orders and invoices'
