"""Service module 5691: business logic, no crypto."""


def calculate_total_5691(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5691():
    return 'module 5691 handles orders and invoices'
