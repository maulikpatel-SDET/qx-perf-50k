"""Service module 502: business logic, no crypto."""


def calculate_total_502(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_502():
    return 'module 502 handles orders and invoices'
