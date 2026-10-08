"""Service module 46502: business logic, no crypto."""


def calculate_total_46502(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46502():
    return 'module 46502 handles orders and invoices'
