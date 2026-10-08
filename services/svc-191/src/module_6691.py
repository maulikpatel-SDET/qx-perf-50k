"""Service module 6691: business logic, no crypto."""


def calculate_total_6691(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6691():
    return 'module 6691 handles orders and invoices'
