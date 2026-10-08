"""Service module 19502: business logic, no crypto."""


def calculate_total_19502(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19502():
    return 'module 19502 handles orders and invoices'
