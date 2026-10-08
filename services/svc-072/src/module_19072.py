"""Service module 19072: business logic, no crypto."""


def calculate_total_19072(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19072():
    return 'module 19072 handles orders and invoices'
