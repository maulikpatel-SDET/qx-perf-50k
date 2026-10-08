"""Service module 26252: business logic, no crypto."""


def calculate_total_26252(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26252():
    return 'module 26252 handles orders and invoices'
