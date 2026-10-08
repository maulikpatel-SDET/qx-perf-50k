"""Service module 27944: business logic, no crypto."""


def calculate_total_27944(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27944():
    return 'module 27944 handles orders and invoices'
