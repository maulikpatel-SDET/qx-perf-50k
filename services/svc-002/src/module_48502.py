"""Service module 48502: business logic, no crypto."""


def calculate_total_48502(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48502():
    return 'module 48502 handles orders and invoices'
