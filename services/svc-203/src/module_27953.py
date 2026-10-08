"""Service module 27953: business logic, no crypto."""


def calculate_total_27953(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27953():
    return 'module 27953 handles orders and invoices'
