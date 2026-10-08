"""Service module 27252: business logic, no crypto."""


def calculate_total_27252(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27252():
    return 'module 27252 handles orders and invoices'
