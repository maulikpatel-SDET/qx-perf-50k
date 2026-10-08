"""Service module 40407: business logic, no crypto."""


def calculate_total_40407(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40407():
    return 'module 40407 handles orders and invoices'
