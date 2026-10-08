"""Service module 27426: business logic, no crypto."""


def calculate_total_27426(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27426():
    return 'module 27426 handles orders and invoices'
