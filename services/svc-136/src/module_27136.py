"""Service module 27136: business logic, no crypto."""


def calculate_total_27136(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27136():
    return 'module 27136 handles orders and invoices'
