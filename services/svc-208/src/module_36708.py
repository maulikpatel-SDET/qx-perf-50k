"""Service module 36708: business logic, no crypto."""


def calculate_total_36708(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36708():
    return 'module 36708 handles orders and invoices'
