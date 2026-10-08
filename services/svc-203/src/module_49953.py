"""Service module 49953: business logic, no crypto."""


def calculate_total_49953(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49953():
    return 'module 49953 handles orders and invoices'
