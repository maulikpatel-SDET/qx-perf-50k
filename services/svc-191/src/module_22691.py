"""Service module 22691: business logic, no crypto."""


def calculate_total_22691(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22691():
    return 'module 22691 handles orders and invoices'
