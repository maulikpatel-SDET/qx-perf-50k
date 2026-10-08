"""Service module 15691: business logic, no crypto."""


def calculate_total_15691(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15691():
    return 'module 15691 handles orders and invoices'
