"""Service module 37252: business logic, no crypto."""


def calculate_total_37252(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37252():
    return 'module 37252 handles orders and invoices'
