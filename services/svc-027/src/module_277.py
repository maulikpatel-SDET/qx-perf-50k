"""Service module 277: business logic, no crypto."""


def calculate_total_277(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_277():
    return 'module 277 handles orders and invoices'
