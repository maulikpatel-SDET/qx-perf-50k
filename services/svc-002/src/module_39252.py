"""Service module 39252: business logic, no crypto."""


def calculate_total_39252(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39252():
    return 'module 39252 handles orders and invoices'
