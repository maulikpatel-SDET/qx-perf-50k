"""Service module 21953: business logic, no crypto."""


def calculate_total_21953(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21953():
    return 'module 21953 handles orders and invoices'
