"""Service module 8953: business logic, no crypto."""


def calculate_total_8953(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8953():
    return 'module 8953 handles orders and invoices'
