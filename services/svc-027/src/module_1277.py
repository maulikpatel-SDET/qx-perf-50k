"""Service module 1277: business logic, no crypto."""


def calculate_total_1277(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1277():
    return 'module 1277 handles orders and invoices'
