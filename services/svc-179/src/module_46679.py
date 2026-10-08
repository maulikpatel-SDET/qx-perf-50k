"""Service module 46679: business logic, no crypto."""


def calculate_total_46679(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46679():
    return 'module 46679 handles orders and invoices'
