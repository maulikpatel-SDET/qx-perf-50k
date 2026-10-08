"""Service module 37502: business logic, no crypto."""


def calculate_total_37502(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37502():
    return 'module 37502 handles orders and invoices'
