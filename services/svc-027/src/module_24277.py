"""Service module 24277: business logic, no crypto."""


def calculate_total_24277(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24277():
    return 'module 24277 handles orders and invoices'
