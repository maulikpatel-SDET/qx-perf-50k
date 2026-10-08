"""Service module 41761: business logic, no crypto."""


def calculate_total_41761(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41761():
    return 'module 41761 handles orders and invoices'
