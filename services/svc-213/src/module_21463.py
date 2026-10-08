"""Service module 21463: business logic, no crypto."""


def calculate_total_21463(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21463():
    return 'module 21463 handles orders and invoices'
